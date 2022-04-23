package ru.lifelaboratory.javavk.controller;

import org.springframework.web.bind.annotation.*;
import ru.lifelaboratory.javavk.entity.Answer;
import ru.lifelaboratory.javavk.entity.Question;
import ru.lifelaboratory.javavk.entity.Response;
import ru.lifelaboratory.javavk.jService.API;
import ru.lifelaboratory.javavk.repository.QuestionRepository;

import java.util.Optional;
import java.util.Random;

@RestController
@RequestMapping(value = "question")
public class QuestionController {

    private final QuestionRepository questionRepository;
    private final API jServiceAPI;

    public QuestionController(QuestionRepository questionRepository, API jServiceAPI) {
        this.questionRepository = questionRepository;
        this.jServiceAPI = jServiceAPI;
    }

    @GetMapping("/random")
    private Response getRandom() {
        Question question = (new Random()).nextBoolean() ? questionRepository.findRandom() : jServiceAPI.getRandomQuestion();
        question.setAnswer(null);
        return new Response(question);
    }

    @PostMapping("/check")
    private Response checkResponse(@RequestBody Answer answer) {
        Optional<Question> findResult = questionRepository.findById(answer.getQuestionId());
        Question question = findResult.isEmpty() ? jServiceAPI.findById(answer.getQuestionId()) : findResult.get();
        if (question == null || question.getAnswer() == null) {
            Response response = new Response();
            response.setValidationError("Not found");
            return response;
        }
        answer.setIsCorrect(question.getAnswer().equals(answer.getAnswer()));
        answer.setCorrectAnswer(question.getAnswer());
        answer.setAnswer(null);
        return new Response(answer);
    }

}
