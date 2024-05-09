
from pyt2s.services import stream_elements

obj = stream_elements.StreamElements()

# Default Voice
data = obj.requestTTS('The quick brown fox jumped over the lazy dog.', 'Linda')

# # Custom Voice
# data = obj.requestTTS('Lorem Ipsum is simply dummy text.', 'Russell')

with open('output.mp3', '+wb') as file:
    file.write(data)
