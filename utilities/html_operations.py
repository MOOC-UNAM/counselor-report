from setup.config import url_location
from datetime import datetime


def current_date_format(date):
    months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    day = date.day
    month = months[date.month - 1]
    year = date.year
    return "{} de {} de {}".format(day, month, year)


def load_head():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bachillerato en Línea Pilares - Informe personalizado</title>
    <link rel="stylesheet" href="{}assets/bootstrap.min.css">
    <link rel="stylesheet" href="{}assets/fonts/stylesheet.css">
    <link rel="stylesheet" href="{}assets/blp.css">
</head>
<body>
    <div class="container">
    """.format(url_location,url_location,url_location)


def student_header(name,lastname,counselor):
    today = current_date_format(datetime.now())

    return """
        <header class="row">
            <table class="table table-borderless table-sm">
                <tr>
                    <td colspan="2" rowspan="3"><img src="assets/blp_logo.jpg" alt="Bachillerato En Línea Pilares" class="img-fluid"></td>
                    <td>informe personalizado de:</td>
                    <td colspan="2">{} {}</td>
                </tr>
                <tr>
                    <td>fecha:</td>
                    <td colspan="2">{}</td>
                </tr>
                <tr>
                    <td>consejería de:</td>
                    <td colspan="2">Lic. {}</td>
                </tr>
                <tr><td></td><td></td><td></td><td></td><td></td></tr>
            </table>
        </header>
    """.format(name.upper(),lastname.upper(),today,counselor)


def resume_score(status,strengths,work,improvement,findings,score):
    general_findings = """
        <li><strong>Dedicar tiempo a diario a su Bachillerato</strong>, calculando que en las asignaturas de este programa requerirá alrededor de 24 horas de dedicación cada semana. Usted irá viendo su ritmo de avance y definirá con exactitud cuánto tiempo le requiere el contenido de cada unidad.</li>
        <li><strong>Preguntar a su asesor cualquier duda</strong> sobre contenidos del curso a través de foros y mensajero, y atender sus orientaciones.</li>
        <li><strong>Comunicar a su consejero</strong> asignado cualquier situación personal, laboral, de salud o que le sea preocupante y que pueda estar afectando su desempeño o avance en el Bachillerato. Por favor, use los foros de la asignatura o el mensajero de la plataforma.</li>
        <li><strong>Responder a todos y cada uno de los mensajes</strong> enviados por su consejero o por su asesor y participar en los foros.</li>
        <li><strong>Revisar a diario su correo electrónico</strong>.</li>
        <li>Apegarse al horario que diseñó para que pueda <strong>dedicar suficiente tiempo de calidad a estudiar su bachillerato</strong>.</li>
    """

    if(status == ''):
        resume_score = """
            <p>Nos dio mucho gusto que haya ingresado en marzo de 2020 al periodo de recursamiento, ya que, en la primera ocasión con la experiencia inicial de aprendizaje, X-ini, el resultado no fue aprobatorio. Su promedio acumulado en este segundo curso es <strong>{}</strong>.</p>
        """.format(score)
        counselor = """
            <p>Las <strong>fortalezas</strong> como aprendiz que hemos detectado son: <span>{}</span></p>
            <p>Desde el área de consejería del Bachillerato, se trabajó en los siguientes aspectos: <span>{}</span></p>
            <p><strong>Algo que es importante mejorar es</strong>: <span>{}</span></p>
        """.format(strengths,work,improvement)
        other_findings = """
            <li>
                <strong>Otras recomendaciones</strong>:
                <div class="row">
                    <div class="col-12" id="otras">{}</div>
                </div>
            </li>
        """.format(findings)
    else:
        resume_score = """
            <p>Nos dio mucho gusto que haya ingresado en marzo de 2020 al periodo de recursamiento, ya que, en la primera ocasión con la experiencia inicial de aprendizaje, X-ini, el resultado no fue aprobatorio.</p>
            <p class="text-center"><strong>{}</strong></p>
        """.format(status)
        counselor = ""
        other_findings = ""
    return """
        <section>
            <div class="row">
                <div class="col">
                    {}
                    {}
                    <p>Las recomendaciones que hacemos, en general, para disfrutar esta experiencia de aprendizaje y lograr la meta son:</p>
                    <ul>
                        {}
                        {}
                    </ul>
                    <p>¡Nos da muchísimo gusto que esté cursando el Bachillerato Policial y esperamos que tenga todo el éxito en esta y todas las demás metas que se haya propuesto! Le deseamos <strong>lo mejor</strong> a usted y a sus seres queridos.</p>
                </div>
            </div>
        </section>
    </div>
</body>
</html>
    """.format(resume_score,counselor,general_findings,other_findings)


def build_html(student):
    html_skeleton = load_head()
    html_skeleton += student_header(student[1],student[0],student[4])
    html_skeleton += resume_score(student[6],student[7],student[8],student[9],student[10],student[11])

    return html_skeleton