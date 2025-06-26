from flask import Blueprint, render_template


#-------------------------------------------Core------------------------------------------------#
core = Blueprint("core",__name__)

@core.route("/", methods=["GET"])
def home_page():
    return render_template("homepage.html")


@core.route("/projects", methods=["GET"])
def projects_page():
    return render_template("projects.html")


@core.route("/skills", methods=["GET"])
def skills_page():
    return render_template("skills.html")


@core.route("/education", methods=["GET"])
def education_page():
    return render_template("education.html")
#-------------------------------------------End-------------------------------------------------#



#-----------------------------------------Sub-Core----------------------------------------------#
@core.route("/projects/project-1", methods=["GET"])
def project1_page():
    return render_template("project1.html")

@core.route("/projects/project-2", methods=["GET"])
def project2_page():
    return render_template("project2.html")

#-------------------------------------------End-------------------------------------------------#