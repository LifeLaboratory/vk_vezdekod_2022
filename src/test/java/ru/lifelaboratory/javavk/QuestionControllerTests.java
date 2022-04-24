package ru.lifelaboratory.javavk;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.web.servlet.MockMvc;
import ru.lifelaboratory.javavk.entity.Answer;
import ru.lifelaboratory.javavk.entity.Question;
import ru.lifelaboratory.javavk.repository.QuestionRepository;

import static org.junit.matchers.JUnitMatchers.containsString;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultHandlers.print;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@RunWith(SpringRunner.class)
@SpringBootTest(classes = JavavkApplication.class)
@AutoConfigureMockMvc
public class QuestionControllerTests {

	@Autowired
	private MockMvc mvc;
	@Autowired
	private QuestionRepository questionRepository;

	@Test
	public void getRandomQuestion() throws Exception {

		mvc.perform(get("/question/random"))
				.andDo(print())
				.andExpect(status().isOk())
				.andExpect(content().string(containsString("OK")));
	}

	@Test
	public void checkQuestion() throws Exception {

		Question question = questionRepository.findRandom();
		System.out.println(question.getAnswer());
		System.out.println(question.getId());
		Answer answer = new Answer(question.getId(), question.getAnswer(), null, null);

		mvc.perform(post("/question/check", answer))
				.andDo(print())
				.andExpect(status().isOk())
				.andExpect(content().string(containsString("OK")));
	}

}
