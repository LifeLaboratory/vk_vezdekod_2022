package ru.lifelaboratory.javavk.jService;

import org.springframework.cache.annotation.Cacheable;
import org.springframework.stereotype.Component;
import org.springframework.web.client.RestTemplate;
import ru.lifelaboratory.javavk.entity.Category;
import ru.lifelaboratory.javavk.entity.Question;
import ru.lifelaboratory.javavk.jService.caching.jQuestionRepository;
import ru.lifelaboratory.javavk.jService.entity.jQuestion;

@Component
public class API implements jQuestionRepository {

    public Question getRandomQuestion() {
        RestTemplate restTemplate = new RestTemplate();
        jQuestion[] jQuestion = restTemplate.getForObject("http://jservice.io/api/random", jQuestion[].class);
        assert jQuestion != null;
        return new Question(
                jQuestion[0].getId(),
                jQuestion[0].getQuestion(),
                new Category(jQuestion[0].getCategory().getId(), jQuestion[0].getCategory().getTitle()),
                jQuestion[0].getValue(),
                null);
    }

    @Override
    @Cacheable(value = "question")
    public Question findById(Long id) {
        return getRandomQuestion();
    }
}
