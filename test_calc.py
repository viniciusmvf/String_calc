from calc import add

def test_string_calc():
	def test_returns_0():
		assert add('') == 0

	def test_returns_bare_numbers():
		assert add('0') == 0
		assert add('1') == 1

	def test_adds_numbers():
		assert add('1,2') == 3
		assert add('1,10') == 11

	def test_describe_delimiters():
		def test_newlines():
			assert add('1\n2') == 3

		def test_can_be_custom():
			assert add('//;\n1;2') == 3
			assert add('//+\n1+10') == 11
			assert add('//abc\n1abc2abc3') == 6

		def test_can_be_mixed():
			assert add('//;\n1,2') == 10

		def test_minus_signs():
			assert add('//-\n-2') == 3

	def test_rejects_negative_numbers():
		assert raises(ValueError, add, '-1')
		assert raises(ValueError, add, '-1,-2')