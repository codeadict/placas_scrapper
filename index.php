<!DOCTYPE html>
<head>
    <meta charset="utf-8" />

     <!-- Set the viewport width to device width for mobile -->
     <meta name="viewport" content="width=device-width" />
    <title>Obtener Datos de Seguro</title>

    <!-- Fix HTML5 Tags on MS monsters-->
    <!--[if lt IE 9]>
    <script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->
</head>
<body>
  <form id="get_placa" method="POST" action="placa.php">
    <label for="placa">Placa:</label>
    <input type="search" id="placa" name="placa" placeholder="Entre el Número de Placa" required/>
    <button class="button" type="submit">Obtener Datos</button>
  </form>
</body>
<!-- vim: set ts=2 et sts=2 sw=2: -->
