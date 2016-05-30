def anagramm(str1, str2):
	if type(str1) != str or type(str2) != str:
		return False
	elif len(str1) == 0 or len(str2) == 0:
		return False
	for c1, c2 in zip(list(str1), zip(str2)):
		if c1[0].isdigit() or c2[0].isdigit():
			return False
	return sorted(list(str1.lower())) == sorted(list(str2.lower()))


def count_letters(strng):
	if type(strng) != str:
		return False
	letter_freq = {}
	for word in strng:
		letter_freq[word] = letter_freq.get(word, 0) + 1
	return letter_freq


