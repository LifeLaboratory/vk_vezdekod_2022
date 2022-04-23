package ru.lifelaboratory.javavk.controller;

import org.springframework.web.bind.annotation.*;
import ru.lifelaboratory.javavk.entity.Answer;
import ru.lifelaboratory.javavk.entity.Question;
import ru.lifelaboratory.javavk.entity.Response;
import ru.lifelaboratory.javavk.repository.QuestionRepository;

import java.util.Optional;

@RestController
@RequestMapping(value = "question")
public class QuestionController {

    private final QuestionRepository questionRepository;

    public QuestionController(QuestionRepository questionRepository) {
        this.questionRepository = questionRepository;
    }

    @GetMapping("/random")
    private Response getRandom() {
        Question question = questionRepository.findRandom();
        question.setAnswer(null);
        return new Response(question);
    }

    @PostMapping("/check")
    private Response checkResponse(@RequestBody Answer answer) {
        Optional<Question> findResult = questionRepository.findById(answer.getQuestionId());
        if (findResult.isEmpty()) {
            Response response = new Response();
            response.setValidationError("Not found");
            return response;
        }
        Question question = findResult.get();
        answer.setIsCorrect(question.getAnswer().equals(answer.getAnswer()));
        answer.setCorrectAnswer(question.getAnswer());
        answer.setAnswer(null);
        return new Response(answer);
    }

}
