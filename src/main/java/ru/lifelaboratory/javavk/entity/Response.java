package ru.lifelaboratory.javavk.entity;

import com.fasterxml.jackson.annotation.JsonInclude;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@JsonInclude(JsonInclude.Include.NON_NULL)
public class Response {

    private enum CODE {
        OK,
        validation_error,
        internal_error;
    }
    private CODE code;
    private String description = null;
    private Object result = null;

    public Response(Object obj) {
        this.result = obj;
        this.code = CODE.OK;
    }

    public void setValidationError(String description) {
        this.code = CODE.validation_error;
        this.description = description;
    }

}
