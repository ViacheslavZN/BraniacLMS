from django.views.generic import TemplateView


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["news_title"]="News headline"
        context [
            "news_preview"
        ]= "Preliminary discription"
        context["range"]=range(5)
        return context


class CoursePageView(TemplateView):
    template_name = "mainapp/course_list.html"


class ContactPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"


class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"
