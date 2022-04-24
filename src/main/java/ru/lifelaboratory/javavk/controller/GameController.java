package ru.lifelaboratory.javavk.controller;

import org.springframework.web.bind.annotation.*;
import ru.lifelaboratory.javavk.entity.Answer;
import ru.lifelaboratory.javavk.entity.Game;
import ru.lifelaboratory.javavk.entity.Question;
import ru.lifelaboratory.javavk.entity.Response;
import ru.lifelaboratory.javavk.jService.API;
import ru.lifelaboratory.javavk.repository.GameRepository;
import ru.lifelaboratory.javavk.repository.QuestionRepository;

import java.util.LinkedList;
import java.util.List;
import java.util.Random;

@RestController
@RequestMapping(value = "game")
public class GameController {

    private final GameRepository gameRepository;
    private final QuestionRepository questionRepository;
    private final API jServiceAPI;

    public GameController(GameRepository gameRepository, QuestionRepository questionRepository, API jServiceAPI) {
        this.gameRepository = gameRepository;
        this.questionRepository = questionRepository;
        this.jServiceAPI = jServiceAPI;
    }

    @PostMapping
    private Response createNewGame(@RequestBody Game newGame) {
        for (int i = 0; i < newGame.getCountQuestions(); i++) {
            newGame.addQuestion((new Random()).nextBoolean() ? questionRepository.findRandom() : jServiceAPI.getRandomQuestion());
        }
        newGame = gameRepository.save(newGame);
        return new Response(newGame);
    }

    @GetMapping("{game_id}/{question_number}")
    private Response getNextQuerstion(@PathVariable("game_id") Long gameId, @PathVariable("question_number") Integer questionNumber) {
        Game game = gameRepository.findById(gameId).get();
        if (game == null) {
            Response response = new Response();
            response.setValidationError("Not found");
            return response;
        }

        Question question = questionRepository.findById(game.getQuestionIdByPosition(questionNumber)).isPresent() ?
                questionRepository.findById(game.getQuestionIdByPosition(questionNumber)).get()
                : jServiceAPI.findById(game.getQuestionIdByPosition(questionNumber));
        return new Response(question);
    }

    @PostMapping("/{game_id}/{question_number}/check")
    private Response checkResponse(@PathVariable("game_id") Long gameId, @PathVariable("question_number") Integer questionNumber, @RequestBody Answer answer) {
        Game game = gameRepository.findById(gameId).get();
        if (game == null) {
            Response response = new Response();
            response.setValidationError("Not found");
            return response;
        }

        Question question = questionRepository.findById(game.getQuestionIdByPosition(questionNumber)).isPresent() ?
                questionRepository.findById(game.getQuestionIdByPosition(questionNumber)).get()
                : jServiceAPI.findById(game.getQuestionIdByPosition(questionNumber));

        answer.setIsCorrect(question.getAnswer().equals(answer.getAnswer()));
        answer.setCorrectAnswer(question.getAnswer());
        answer.setAnswer(null);
        return new Response(answer);
    }

    @PostMapping("/{game_id}/finish")
    private Response checkResponse(@PathVariable("game_id") Long gameId) {
        Game game = gameRepository.findById(gameId).get();
        List<Answer> answers = new LinkedList<>();
        for (int i = 0; i < game.getCountQuestions(); i++) {
            Question question = questionRepository.findById(game.getQuestionIdByPosition(i)).isPresent() ?
                    questionRepository.findById(game.getQuestionIdByPosition(i)).get()
                    : jServiceAPI.findById(game.getQuestionIdByPosition(i));

            Answer answer = new Answer();
            answer.setCorrectAnswer(question.getAnswer());
            answers.add(answer);
        }

        return new Response(answers);
    }

}
