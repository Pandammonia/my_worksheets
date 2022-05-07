from survey import AnonymousSurvey

# define queation
question = 'What language did you learn to speak first?'
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("Enter 'q' to leave at any time")
while True:
	response = input("Langauge: ")
	if response == 'q':
		break
	my_survey.store_response(response)

#show result
print("Thank you for taking part in this survey!")
my_survey.show_results()
