package ru.lifelaboratory.javavk.entity;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.*;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
@JsonInclude(JsonInclude.Include.NON_NULL)
public class Answer {

    @JsonProperty(value = "question_id")
    private Long questionId;
    private String answer;
    @JsonProperty(value = "is_correct")
    private Boolean isCorrect;
    @JsonProperty(value = "correct_answer")
    private String correctAnswer;

}
