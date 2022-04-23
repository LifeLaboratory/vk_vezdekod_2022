package ru.lifelaboratory.javavk.repository;

import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;
import ru.lifelaboratory.javavk.entity.Question;

import java.util.Optional;

@Repository
public interface QuestionRepository extends CrudRepository<Question, Long> {

    @Query(nativeQuery = true, value = "SELECT * FROM question ORDER BY RAND() LIMIT 1")
    Question findRandom();

    @Override
    Optional<Question> findById(Long id);

}
