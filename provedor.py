<!DOCTYPE html>
<html lang="pt-br">
<body>
  <h1>Módulos de {{ tema }}</h1>
  <ul>
    {% for m in modulos %}
    <li>{{ m }}</li>
    {% endfor %}
  </ul>
</body></html>
