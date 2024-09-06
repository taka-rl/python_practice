from difflib import SequenceMatcher
from datetime import datetime
from typing import Dict, Any


class ChatBot:
    DEFAULT_ANSWER: str = 'Sorry, I didn\'t understand that'
    THRESHOLD: float = 0.5

    def __init__(self, name: str, responses: dict[str, str]) -> None:
        self.name = name
        self.responses = responses

    @staticmethod
    def calculate_similarity(input_sentence: str, response_sentence: str) -> float:
        sequence: SequenceMatcher = SequenceMatcher(a=input_sentence, b=response_sentence)
        return sequence.ratio()

    def get_best_response(self, user_input: str) -> tuple[str, float]:
        highest_similarity: float = 0.0
        best_match: str = self.DEFAULT_ANSWER

        for response in self.responses:
            similarity: float = self.calculate_similarity(user_input, response)
            if similarity > self.THRESHOLD:
                highest_similarity = similarity
                best_match: str = self.responses[response]

        return best_match, highest_similarity

    @staticmethod
    def get_weather_info(location: str) -> dict[str, Any]:
        """
        Return the weather information depending on the location through OpenWeather API
        About URL setting: https://openweathermap.org/current#builtin

        Parameters:
            location (str): the location

        Returns:
            dict: the weather information
        """
        import requests

        api_key = 'your_api_key_here'  # Replace 'your_api_key_here' with your actual OpenWeatherMap API key
        url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'

        # Get the information
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()  # Parse the JSON response

            weather_data = {'Temperature': data['main']['temp'], 'Wind Speed': data['wind']['speed'],
                            'Pressure': data['main']['pressure'], 'Humidity': data['main']['humidity'],
                            'Description': data['weather'][0]['description']}

            return weather_data
        else:
            # Print error message with status code
            print(f"Error: Unable to fetch data for {location}. HTTP Status code: {response.status_code}")
            if response.status_code == 401:
                print("Unauthorized: Check if your API key is correct.")
            elif response.status_code == 404:
                print("City not found: Please check the city name and try again.")
            else:
                print("An unexpected error occurred.")

    def run(self) -> None:
        print(f'Hello!, My name is {self.name}, how can I help you?')
        print(f'If you would like to finish, write exit or quit or bye')

        while 1:
            user_input: str = input('You: ')
            response, similarity = self.get_best_response(user_input)

            if user_input.lower() in ['exit', 'quit', 'bye']:
                print('Chatbot ends')
                break

            if response == 'GET_TIME':
                response = f'The time is: {datetime.now():%H:%M}'

            if response == 'GET_WEATHER':
                print("Get the weather information")
                location: str = input('Enter the location for the weather information: ')
                weather_info = self.get_weather_info(location)

                if weather_info:
                    print(f'The weather information in {location} is as follows: ')
                    response = weather_info
                else:
                    response = 'Sorry, I could not retrieve the weather information at the moment.'

            print(f'{self.name}: {response} (Similarity: {similarity:.2%})')


def main() -> None:
    responses: dict[str, str] = {
        'hello': 'Hello! How are you today?',
        'how are you': 'Great, thanks! What about you?',
        'what time is it': 'GET_TIME',
        'bye': 'Goodbye! Have a great day!',
        'quit'
        'what is the weather': 'GET_WEATHER'

    }

    chatbot: ChatBot = ChatBot(name='Tom', responses=responses)
    chatbot.run()


if __name__ == '__main__':
    main()
