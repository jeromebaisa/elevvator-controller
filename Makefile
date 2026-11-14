.PHONY: run test

run:
	python3 elevator.py

test:
	@for file in tests/*.in; do \
		echo "Testing $$file"; \
		python3 elevator.py < "$$file" > "$${file%.in}.actual"; \
		diff "$${file%.in}.expected" "$${file%.in}.actual" || exit 1; \
	done
	@echo "All tests passed!"
