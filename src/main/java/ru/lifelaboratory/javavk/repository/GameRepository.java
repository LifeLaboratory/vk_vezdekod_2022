package ru.lifelaboratory.javavk.repository;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;
import ru.lifelaboratory.javavk.entity.Game;

import java.util.Optional;

@Repository
public interface GameRepository extends CrudRepository<Game, Long> {

    @Override
    Optional<Game> findById(Long id);

}
