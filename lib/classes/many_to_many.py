class Article:
    all= []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        self.__class__.all.append(self)
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        if isinstance(value, str) and 5 <= len(value) <= 50 and not hasattr(self, "title"):
             self._title = value
        else:
            raise Exception("Title must be a string between 5 and 50 characters long.")
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, value):
        if isinstance(value, Author):
           self._author = value
        else:
            raise Exception
    @property
    def magazine(self):
        return self._magazine
    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
           self._magazine = value
        else:
            raise Exception
class Author:
    def __init__(self, name):
        self.name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0 and not hasattr(self, "name"):
           self._name = value
        else:
            raise Exception("Name already exists.")
    def articles(self):
        return  [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        categories= list(set([magazine.category for magazine in self.magazines()]))
        return categories if categories else None
class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
             self._name = value
        else:
            raise Exception("Name must be a string between 2 and 16 characters long.")
    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
             self._category = value
        else:
            raise Exception("Category must be a string greater than 0 characters long.")
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set([article.author for article in self.articles()]))

    def article_titles(self):
        articles= list(set([article.title for article in self.articles()]))
        return articles if articles else None
    def contributing_authors(self):
     contributing_authors = [
        author for author in set(article.author for article in self.articles())
        if sum(1 for article in self.articles() if article.author == author) > 2
        ]
     return contributing_authors if contributing_authors else None        