class Paginator:
    def __init__(self):
        self._pages = []
        self.currentPage = ''

    def addLine(self, line: str):
        lineCharCount = len(line) + 1  # plus one for newline
        if len(self.currentPage) + lineCharCount >= 2000:
            self._closePage()
        self.currentPage += line + '\n'

    def _closePage(self):
        if self.currentPage != '':
            self._pages.append(self.currentPage)
        self.currentPage = ''

    @property
    def pages(self):
        self._closePage()
        return self._pages
