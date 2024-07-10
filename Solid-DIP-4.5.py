# class Book:
#    def read(self):
#        print("Book is reading")

# class StoryReader:
#    def __init__(self):
#        self.book = Book()

#    def tell_story(self):
#        self.book.read()

from abc import ABC, abstractmethod


class StorySource(ABC):
    @abstractmethod
    def get_story(self):
        pass


class Book(StorySource):
    def get_story(self):
        print("Book is reading")


class AudioBook(StorySource):
    def get_story(self):
        print("Book is reading by audio")


class StoryReader:
    def __init__(self, story_source: StorySource):
        self.story_source = story_source

    def tell_story(self):
        self.story_source.get_story()


book = Book()
audiobook = AudioBook()
readerAudioBook = StoryReader(audiobook)

readerBook = StoryReader(book)

readerAudioBook.tell_story()
readerBook.tell_story()


