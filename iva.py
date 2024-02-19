def calcular_total_factura(cantidad_sin_iva, porcentaje_iva=21):
    """Calcula el total de una factura después de aplicarle el IVA."""
    iva = cantidad_sin_iva * (porcentaje_iva / 100)
    total_con_iva = cantidad_sin_iva + iva
    return total_con_iva