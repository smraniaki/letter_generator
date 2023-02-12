def generate_letter():
    company_name = input("Enter the company name: ")
    your_name = input("what is your name:")
    letter = f"""Dear Sir/Madam,

I am writing to express my interest in the opportunity to define my master thesis topic in line with the activities of your company, {company_name}, and the possibility of an internship while doing my masters.

As a student of engineering science with a background in business data analytics using Python and Tableau, database management using SQL, and building and deploying predictive machine learning models using classical statistical methods and neural networks including deep learning approach, I believe I could bring valuable contributions to {company_name}. 

I have eight years of experience as a project manager and data analyst in different sectors such as the oil and gas industry, which has equipped me well with the challenges in work environment dynamics and agile requirements. This experience, combined with my strong academic background, makes me confident in my ability to handle complex data analysis projects and contribute positively to the success of {company_name}.

I am particularly interested in using the valuable data and resources of {company_name}, such as knowledge sharing with the company's experts, for the successful accomplishment of my thesis. I assure you that any data I use for my thesis will only be used for {company_name}'s needs and will not be disclosed outside the company under any circumstances unless I am advised otherwise.

Financial gain is not very important to me at this time and I am primarily motivated by the opportunity to gain practical experience and have hands-on experience in the field of data analysis. I believe that an internship at {company_name} would provide me with a unique opportunity to not only advance my knowledge and skills, but also contribute to the success of your organization.

Thank you for considering my application. I look forward to the opportunity to discuss my qualifications further and answer any questions you may have.

Sincerely,
{your_name}"""
    return letter

generated_letter = generate_letter()
print(generated_letter)