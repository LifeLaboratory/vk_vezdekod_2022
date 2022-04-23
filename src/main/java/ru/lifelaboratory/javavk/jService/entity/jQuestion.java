package ru.lifelaboratory.javavk.jService.entity;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Data;

@Data
public class jQuestion {

    private Long id;
    private String answer;
    private String question;
    private Integer value;
    private jCategory category;

}
