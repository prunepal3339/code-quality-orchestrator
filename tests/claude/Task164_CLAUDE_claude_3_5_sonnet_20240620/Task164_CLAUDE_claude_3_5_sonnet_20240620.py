import unittest
# from output.claude.Task164_CLAUDE_claude_3_5_sonnet_20240620 import lastNameLensort as lastNameLensort
# from output.codestral.Task164_MISTRAL_codestral_latest import last_name_len_sort as lastNameLensort
# from output.gemini.Task164_GEMINI_gemini_1_5_pro_001 import  lastNameLensort as lastNameLensort
# from output.gtp4o.Task164_OPENAI_gpt_4o import  lastNameLensort as lastNameLensort
# from output.llama3.Task164_PERPLEXITY_llama_3_sonar_large_32k_chat import  lastNameLensort as lastNameLensort

class TestLastNameLensort(unittest.TestCase):

    def test_various_last_name_lengths(self):
        names = [
            "Jennifer Figueroa",
            "Heather Mcgee",
            "Amanda Schwartz",
            "Nicole Yoder",
            "Melissa Hoffman"
        ]
        expected = ["Heather Mcgee", "Nicole Yoder", "Melissa Hoffman", "Jennifer Figueroa", "Amanda Schwartz"]
        self.assertEqual(lastNameLensort(names), expected)

    def test_same_last_name_length(self):
        names = [
            "John Doe",
            "Alice Lee",
            "Bob Zee",
            "Carol Foe"
        ]
        expected = ["Bob Zee", "Alice Lee", "Carol Foe", "John Doe"]
        self.assertEqual(lastNameLensort(names), expected)

    def test_single_name(self):
        names = ["James Bond"]
        expected = ["James Bond"]
        self.assertEqual(lastNameLensort(names), expected)

    def test_multiple_names_same_last_name_length(self):
        names = [
            "Tom Jones",
            "Jerry Jones",
            "Rick Jones",
            "Bob Smith",
            "Paul Smith"
        ]
        expected = ["Bob Smith", "Paul Smith", "Tom Jones", "Jerry Jones", "Rick Jones"]
        self.assertEqual(lastNameLensort(names), expected)

    def test_single_letter_last_names(self):
        names = [
            "A B",
            "C D",
            "E F",
            "G H",
            "I J"
        ]
        expected = ["A B", "C D", "E F", "G H", "I J"]
        self.assertEqual(lastNameLensort(names), expected)

    def test_varied_last_name_lengths(self):
        names = [
            "A B",
            "C Def",
            "E Fghij",
            "G Hijklmn",
            "I J"
        ]
        expected = ['A B', 'I J', 'C Def', 'E Fghij', 'G Hijklmn']
        self.assertEqual(lastNameLensort(names), expected)

    def test_long_last_names(self):
        names = [
            "Anna Longnamehere",
            "Bob Shortname",
            "Carl Mediumname",
            "Dave Longestnamehere"
        ]
        expected = ["Bob Shortname", "Carl Mediumname", "Anna Longnamehere", "Dave Longestnamehere"]
        self.assertEqual(lastNameLensort(names), expected)

    def test_varying_lengths(self):
        names = [
            "Alice Wonderland",
            "Bob Marley",
            "Charlie Brown",
            "David Bowie",
            "Edward Norton"
        ]
        expected = ["Bob Marley", "David Bowie", "Charlie Brown", "Edward Norton", "Alice Wonderland"]
        self.assertEqual(lastNameLensort(names), expected)

    def test_names_with_punctuation(self):
        names = ["James Brown","Elijah Davis","Noah Johnson","Liam O'Neill","Oliver Smith"]
        expected = ["James Brown","Elijah Davis","Noah Johnson","Liam O'Neill","Oliver Smith"]
        print(lastNameLensort(names))
        self.assertEqual(lastNameLensort(names), expected)

    def test_already_sorted_names(self):
        names = [
            "Aaron Smith",
            "Brad Jones",
            "Chris Lee",
            "Derek Adams",
            "Evan Brown"
        ]
        expected = ["Chris Lee", "Brad Jones", "Aaron Smith", "Derek Adams", "Evan Brown"]
        self.assertEqual(lastNameLensort(names), expected)

if __name__ == '__main__':
    unittest.main()