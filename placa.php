<?php
//Setear encoding a UTF8
ini_set("default_charset", "utf-8");

$placa = $_POST['placa'];

echo $placa;

exec('python get_placa.py ' . escapeshellcmd($placa), $salida);

echo $salida;

$obj = json_decode($salida);

print "<h1>DATOS OBTENIDOS</h1>"
print "Placa: " . $obj->{'placa'} . "\n";
print "Aseguradora: " . $obj->{'aseguradora'} . "\n";
print "Num. Certificado: " . $obj->{'no_certificado'} . "\n";
print "Fecha Inicio: " . $obj->{'f_inicio'} . "\n";
print "Fecha Fin: " . $obj->{'f_fin'} . "\n";
print "Vigente: " . $obj->{'vigencia'} . "\n";

?>
