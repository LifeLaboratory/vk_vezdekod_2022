package ru.lifelaboratory.javavk.entity;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.*;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

@Entity
@Getter
@Setter
@ToString
@AllArgsConstructor
@NoArgsConstructor
@JsonInclude(JsonInclude.Include.NON_NULL)
public class Game {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    @JsonProperty(value = "count_questions")
    private Integer countQuestions;
    @JsonProperty(value = "min_difficulty")
    private Integer minDifficulty;
    @JsonProperty(value = "max_difficulty")
    private Integer maxDifficulty;
    @JsonProperty(value = "questions_id")
    private String questionsId;

    public void addQuestion (Question question) {
        if (this.questionsId == null) {
            this.questionsId = "";
        }
        this.questionsId += question.getId().toString() + ",";
    }

    public Long getQuestionIdByPosition (Integer position) {
        String[] ids = this.questionsId.split(",");
        return Long.valueOf(ids[position]);
    }

}
