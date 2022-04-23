package ru.lifelaboratory.javavk;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cache.annotation.EnableCaching;

@SpringBootApplication
@EnableCaching
public class JavavkApplication {

	public static void main(String[] args) {
		SpringApplication.run(JavavkApplication.class, args);
	}

}
