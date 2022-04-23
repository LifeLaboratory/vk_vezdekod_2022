package ru.lifelaboratory.javavk.jService.caching;

import ru.lifelaboratory.javavk.entity.Question;

public interface jQuestionRepository {

    Question findById(Long id);

}
