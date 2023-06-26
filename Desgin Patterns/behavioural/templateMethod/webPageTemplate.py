class WebPageTemplate:
    def renderHeader(self):
        raise NotImplementedError()

    def renderBody(self):
        raise NotImplementedError()

    def renderFooter(self):
        raise NotImplementedError()

    def renderPage(self):
        self.renderHeader()
        self.renderBody()
        self.renderFooter()


class HomePage(WebPageTemplate):
    def renderHeader(self):
        print("Rendering Home Page Header")

    def renderBody(self):
        print("Rendering Home Page Body")

    def renderFooter(self):
        print("Rendering Home Page Footer")


class AboutPage(WebPageTemplate):
    def renderHeader(self):
        print("Rendering About Page Header")

    def renderBody(self):
        print("Rendering About Page Body")

    def renderFooter(self):
        print("Rendering About Page Footer")


# Usage
homePage = HomePage()
homePage.renderPage()
# Output:
# Rendering Home Page Header
# Rendering Home Page Body
# Rendering Home Page Footer

aboutPage = AboutPage()
aboutPage.renderPage()
# Output:
# Rendering About Page Header
# Rendering About Page Body
# Rendering About Page Footer
