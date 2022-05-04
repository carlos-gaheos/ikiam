from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class FichaSocioeconomica(models.Model):
    _name = "ficha.socioeconomica"
    _description = "Ficha Socioeconomica"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    state = fields.Selection([
        ('aprobada', 'Aprobada'),
        ('rechazada', 'Rechazada'),
        ('pendiente', 'Pendiente'),
        ('borrador', 'Borrador'),
    ], 'Estado', default='borrador')
    cedula = fields.Char(strin="Cédula")
    nombres = fields.Char(strin="Nombres")
    apellidos = fields.Char(strin="Apellidos")
    fecha_nacimiento = fields.Date(string="Fecha de Nacimiento")
    edad = fields.Integer(string="Edad")
    genero = fields.Selection([
        ('m', 'Masculino'),
        ('f', 'Femenino'),
        ('o', 'Otro')
    ], 'Genero', required=True, default='m')
    sangre = fields.Selection([
        ('A+', 'A+ve'),
        ('B+', 'B+ve'),
        ('O+', 'O+ve'),
        ('AB+', 'AB+ve'),
        ('A-', 'A-ve'),
        ('B-', 'B-ve'),
        ('O-', 'O-ve'),
        ('AB-', 'AB-ve')
    ], string='Tipo de Sangre')

    provincia = fields.Char(string="Provincia")
    canton = fields.Char(string="Canton")
    parroquia = fields.Char(string="Parroquia")
    tipo_discapacidad = fields.Selection([
        ('n', 'Ninguna'),
        ('f', 'Fisica'),
        ('a', 'Auditiva'),
        ('v', 'Visual'),
    ], 'Tipo de discapacidad', required=True, default='n')
    porcentaje_discapacidad = fields.Float('Porcentaje', digits=(2, 2))
    carnet_conadis = fields.Char(string="N° de carnet")
    carnet_attachment = fields.Binary(string="Carnet")
    alergias = fields.Char(string="Alergias")
    email_personal = fields.Char(string="Correo personal")
    email_institucional = fields.Char(string="Correo Institucional")
    celular = fields.Char(string="N° Celular")
    tel_fijo = fields.Char(string="N° Telefóno Fijo")
    etnia = fields.Selection([
        ('a', 'Afroecuatoriana'),
        ('m', 'Mestizo'),
        ('b', 'Blanco'),
        ('i', 'Indigena'),
        ('m', 'Montuvio'),
        ('o', 'Otros')
    ], 'Etnia', required=True, default='m')
    nacionalidad = fields.Char(string="Nacionalidad")
    estado_civil = fields.Selection([
        ('c', 'Casado'),
        ('d', 'Divorciado'),
        ('s', 'Soltero'),
        ('u', 'Union Libre'),
        ('v', 'Viudo')
    ], 'Estado Civil', required=True, default='s')

    ##relacion familiares
    familiares_lines = fields.One2many('familiar', 'ficha_id')
    enfermedad_lines = fields.One2many('enfermedad', 'ficha_id')
    ayudaterceros_lines = fields.One2many('ayuda.tercera', 'ficha_id')
    familiar_ingresos_lines = fields.One2many('familiar.ingresos', 'ficha_id')
    vehiculos_lines = fields.One2many('vehiculos', 'ficha_id')
    vivienda_lines = fields.One2many('vivienda', 'ficha_id')


    estructura_familiar = fields.Selection([
        ('fe', 'FAMILIA ENSAMBLADA (CONFORMADA POR PADRES DIVORCIADOS, VIUDOS O SEPARADOS, Y SUS HIJOS DE UNIONES ANTERIORES)'),
        ('fex', 'FAMILIA EXTENSA (CONFORMADA POR ABUELOS, TÍOS, PRIMOS Y OTROS PARIENTES CONSANGUÍNEOS O AFINES)'),
        ('fh', 'FAMILIA HOMOPARENTAL (CONFORMADA POR AQUELLA PAREJA DE HOMBRES O DE MUJERES QUE SON TUTORES DE UNO O MÁS NIÑOS)'),
        ('fm', 'FAMILIA MONOPARENTAL (EN LA QUE EL HIJO O HIJOS VIVEN CON UN SOLO PROGENITOR YA SEA LA MADRE O EL PADRE)'),
        ('fn', 'FAMILIA NUCLEAR (FORMADA POR LOS PROGENITORES Y UNO O MÁS HIJOS)'),
        ('fu', 'FAMILIA UNIPERSONAL (CONFORMADA POR UNA SOLA PERSONA) '),
        ('fps', 'LA FAMILIA DE PADRES SEPARADOS (EN LA QUE LOS PADRES SE NIEGAN A VIVIR JUNTOS O NO SON PAREJA PERO DEBEN SEGUIR CUMPLIENDO SU ROL DE PADRES ANTE LOS HIJOS POR MUY DISTANTES QUE ESTOS SE ENCUENTREN)'),
    ], 'Estructura Familiar', required=True, default='fn')

    contacto_emergencia = fields.Char(string="Nombres Completos")
    dir_contacto_emergencia = fields.Char(string="Direccion")
    telf_contacto_emergencia = fields.Char(string="Teléfono fijo")
    cel_contacto_emergencia = fields.Char(string="Celular")
    correo_contacto_emergencia = fields.Char(string="Correo")


    colegio_anterior = fields.Char(string="Nombre del colegio que proviene")
    tipo_sostenimiento = fields.Selection([
        ('m', 'Municipal'),
        ('g', 'Fiscal'),
        ('f', 'Fiscomicional'),
        ('p', 'Particular'),
    ], 'Tipo de sostenimiento', required=True, default='m')
    pais_colegio = fields.Many2one('res.country', string='Pais')
    provincia_colegio = fields.Char(string="Provincia")
    canton_colegio = fields.Char(string="Canton")
    parroquia_colegio = fields.Char(string="Parroquia")
    tipo_bachillerato = fields.Selection([
        ('b', 'Bachillerato General Unificado'),
        ('g', 'Otros'),
    ], 'Tipo de bachillerato', required=True, default='g')
    fecha_graduacion = fields.Date(string="Fecha de graduación")
    calificacion = fields.Float(string="Calificación de grado", digits=(3,2))
    puntaje_bachiller = fields.Float(string="Puntaje de quiero ser bachiller", digits=(3,2))
    acta_grado = fields.Binary('Acta de Grado')
    abanderado = fields.Boolean('Fue abanderado o escolta', default=False)
    acta_abanderado = fields.Binary('Acta', help="Subir acta de designación de abanderado o escolta")

    ###DATOS DOMICILIARIOS
    pais_procedencia = fields.Many2one('res.country', 'Pais')
    provincia_procedencia = fields.Char(string="Provincia")
    canton_procedencia = fields.Char(string="Canton")
    parroquia_procedencia = fields.Char(string="Parroquia")
    barrio_procedencia = fields.Char("Barrio/Sector")
    callep_procedencia = fields.Char("Calles o Av. Principal")
    calles_procedencia = fields.Char("Calles o Av. Secundaria")
    casa_procedencia = fields.Char("Nro. Casa")
    referencia_procedencia = fields.Char("Referencia, frente o a lado de")

    ###DATOS DOMICILIARIOS NAPO
    pais_procedencian = fields.Many2one('res.country', 'Pais')
    provincia_procedencian = fields.Char(string="Provincia")
    canton_procedencian = fields.Char(string="Canton")
    parroquia_procedencian = fields.Char(string="Parroquia")
    barrio_procedencian = fields.Char("Barrio/Sector")
    callep_procedencian = fields.Char("Calles o Av. Principal")
    calles_procedencian = fields.Char("Calles o Av. Secundaria")
    casa_procedencian = fields.Char("Nro. Casa")
    referencia_procedencian = fields.Char("Referencia, frente o a lado de")

    ###DATOS ECONOMICOS
    fondos_propios = fields.Boolean('Fondos propios', default=False)
    ayuda_padres = fields.Boolean('Ayuda de sus padres', default=False)
    credito_educativo = fields.Boolean('Crédito educativo', default=False)
    entidad_financiera = fields.Char("Entidad financiera")
    monto_credito = fields.Float("Monto", digits=(6,2))
    trabajo = fields.Boolean('Usted trabaja?', default=False)
    ocupacion = fields.Char('Ocupación')
    nombre_empresa = fields.Char('Nombre de la empresa')
    direccion_empresa = fields.Char('Dirección del lugar de trabajo')
    remuneracion = fields.Float("Remuneración", digits=(6,2))
    cabeza_familia = fields.Boolean('Eres cabeza familiar',default=False)
    personas_cargo = fields.Integer('N° de personas a cargo')
    ahorros = fields.Boolean('Posees ahorros en entidades financieras?',default=False)
    cantidad_ahorros = fields.Float('Cuanto?',digits=(6,2))
    parentezco_econo = fields.Selection([
        ('a', 'Abuelo/a'),
        ('c', 'Conyugue'),
        ('h', 'Hermano/a'),
        ('hj', 'Hijo/a'),
        ('m', 'Madre'),
        ('p', 'Padre'),
        ('s', 'Sobrino/a'),
        ('t', 'Tio/a'),
        ('o', 'Otros'),
        ('n', 'Nadie'),
    ], 'De quien dependes económicamente ?', required=True, default='n')
    tiene_negocio = fields.Boolean('La familia posee negocio', default=False)
    tipo_negocio = fields.Char('Indique que tipo de negocio')


    ##EGRESOS
    alimentacion = fields.Float('Alimentación',digits=(6,2))
    arriendo = fields.Float('Alquiler de vivienda (si arriendan)',digits=(6,2))
    transporte = fields.Float('Transporte', digits=(6, 2))
    educacion = fields.Float('Educación', digits=(6, 2))
    servicios_basicos = fields.Float('Servicios básicos (agua, luz, teléfono etc.)', digits=(6, 2))
    educacion = fields.Float('Salud', digits=(6, 2))
    vestuario = fields.Float('Vestuario', digits=(6, 2))
    otros_egresos = fields.Float('Otros', digits=(6, 2))

    ##RESUMEN
    total_ingresos = fields.Float('Total de ingresos', digits=(6, 2))
    total_egresos = fields.Float('Total de egresos', digits=(6, 2))
    saldo = fields.Float('Saldo', digits=(6, 2))

    ####Características de la vivienda del hogar
    vivienda_es = fields.Selection([
        ('a', 'Arrendada'),
        ('s', 'Por Servicios'),
        ('p', 'Prestada o cedida'),
        ('pp', 'Propia y la estan pagando'),
        ('pt', 'Propia y totalmente pagada'),
    ], 'La vivienda es?', required=True, default='a')
    vivienda_tipo = fields.Selection([
        ('p2', 'Casa dos pisos'),
        ('p1', 'Casa de una planta'),
        ('ch', 'Choza'),
        ('co', 'Covacha'),
        ('ct', 'Cuarto'),
        ('dp', 'Departamento'),
        ('ma', 'Mediagua'),
        ('md', 'Minidepartamento'),
        ('r', 'Rancho'),

    ], 'Tipo de vivienda', required=True, default='dp')
    tipo_construccion = fields.Selection([
        ('a', 'Adobe'),
        ('ag', 'Aglomerado'),
        ('b', 'Bloque'),
        ('c', 'Caña'),
        ('ct', 'Concreto'),
        ('l', 'Ladrillo'),
        ('m', 'Madera'),
        ('mb', 'Madera y bloque'),

    ], 'Tipo de construción', required=True, default='ct')
    ubicacion_vivienda = fields.Selection([
            ('r', 'Zona Rural'),
            ('u', 'Zona Urbana'),
        ], 'Ubicación de la vivienda donde viven / sector?', required=True, default='r')

    ##Describa internamente la vivienda
    sala = fields.Boolean('Sala', default=False)
    comedor = fields.Boolean('Comedor', default=False)
    cocina = fields.Boolean('Cocina', default=False)
    asadero = fields.Boolean('Asadero', default=False)
    cant_banos = fields.Integer('N° de baños')
    cant_dormitorios = fields.Integer('Número de dormitorios')

    ##Menaje de hogar
    cocina_induccion = fields.Boolean('Cocina de inducción', default=False)
    cocina_gas = fields.Boolean('Cocina a gas', default=False)
    cocineta = fields.Boolean('Cocineta', default=False)
    lavadora = fields.Boolean('Lavadora', default=False)
    secadora = fields.Boolean('Secadora', default=False)
    refrigeradora = fields.Boolean('Refrigeradora', default=False)
    licuadora = fields.Boolean('Licuadora', default=False)
    microondas = fields.Boolean('Microondas', default=False)
    equipo_sonido = fields.Boolean('Equipo de sonido', default=False)
    tv_cable = fields.Boolean('Tv cable', default=False)
    directv = fields.Boolean('Directv', default=False)
    computador_escritorio = fields.Boolean('Computadora de escritorio', default=False)
    laptop_tiene = fields.Boolean('Computadora portatil', default=False)
    tablet_tiene = fields.Boolean('Tablet', default=False)
    celular_tiene = fields.Boolean('Teléfono celular', default=False)
    cant_tv = fields.Integer("Cuantas Tv a color")
    tv_smart = fields.Boolean('Tv Smart', default=False)
    tcaint = fields.Boolean('Teléfono celular con acceso a internet', default=False)
    radio = fields.Boolean('Radio', default=False)
    internet = fields.Boolean('Internet', default=False)

    operadora_internet = fields.Selection([
        ('m', 'Movistar'),
        ('c', 'Claro'),
        ('cnt', 'CNT'),
        ('t', 'Twenti'),
        ('o', 'Otro'),
    ], 'Operadora de internet', required=True, default='cnt')
    tipo_acceso_internet = fields.Selection([
        ('a', 'Acceso telefónico (ADLS o fibra óptica) o cable'),
        ('o', 'Otro'),
    ], '¿De qué forma es la conexión de internet en su vivienda?', required=True, default='o')
    cant_internet = fields.Selection([
            ('1', 'Comaprto con 1 persona'),
            ('2', 'Comaprto con 2 personas'),
            ('3', 'Comaprto con 3 personas'),
            ('4', 'Mas de 3 personas'),
            ('0', 'Nadie'),
        ], '¿En caso de compartir los dispositivos de acceso a internet en su vivienda, ¿con cuantas personas comparte?',required=True, default='0')
    velc_internet = fields.Selection([
                ('15', 'Tecnología - Cobre 11 - 15 Mbps'),
                ('20', 'Tecnología - Cobre 11 - 20 Mbps'),
                ('30', 'Tecnología - Cobre 11 - 30 Mbps'),
                ('50', 'Tecnología - Cobre 11 - 50 Mbps'),
                ('70', 'Tecnología - Cobre 11 - 70 Mbps'),
                ('100', 'Tecnología - Cobre 11 - 100 Mbps'),
                ('150', 'Mas de 100 Mbps'),
                ('0', 'Ninguna'),

            ], '¿En caso de compartir los dispositivos de acceso a internet en su vivienda, ¿con cuantas personas comparte?', required=True, default='0')
    disp_acceso_internet = fields.Selection([
        ('i', 'Ilimitado (todo el tiempo)'),
        ('l', 'limitado'),
        ('o', 'Otro'),
    ], 'Su disponibilidad de acceso a internet es', required=True, default='i')
    cant_estud = fields.Integer('Personas del hogar estudiando, o teletrabando')
    cant_conect = fields.Integer('Personas conectadas a internet simultáneamente')

    ###Servicios básicos que cuenta la vivienda:
    electricidad = fields.Boolean('Servicios de electricidad', default=False)
    agua_potable = fields.Boolean('Servicios de agua potable', default=False)
    alcantarillado = fields.Boolean('Servicios de alcantarillado', default=False)
    alumbrado = fields.Boolean('Servicios de alumbrado público', default=False)
    convencional = fields.Boolean('Teléfono convencional', default=False)

    ######Becas y otros
    recibe_becas = fields.Boolean('Recibe beca o ayuda económica?', default=False)
    institu_bec = fields.Char('Indique la institución')
    monto_bec = fields.Float('Monto', digits=(6,2))
    periodo  = fields.Selection([
        ('a', 'Anual)'),
        ('m', 'Mensual'),
        ('s', 'Semestral'),
        ('n', 'Ninguno'),
    ], 'Período', required=True, default='n')
    eres_deportista = fields.Boolean('Eres deportista de alto rendimiento?', default=False)
    certi_dept = fields.Binary('Certificado')

class Familiar(models.Model):
    _name = "familiar"
    _description = "Familiar"

    nombre = fields.Char('Nombres Completos')
    cedula = fields.Char('Cédula')
    parentezco = fields.Selection([
        ('a', 'Abuelo/a'),
        ('c', 'Conyugue'),
        ('h', 'Hermano/a'),
        ('hj', 'Hijo/a'),
        ('m', 'Madre'),
        ('p', 'Padre'),
        ('s', 'Sobrino/a'),
        ('t', 'Tio/a'),
        ('o', 'Otros'),
    ], 'Parentesco', required=True, default='o')
    ingresos = fields.Float('Ingresos', digits=(7, 2))
    ficha_id = fields.Many2one('ficha.socioeconomica')

class Enfermedad(models.Model):
    _name = "enfermedad"
    _description = "Enfermedad"

    nombre = fields.Char('Enfermedad')
    observacion = fields.Char('observaciones')
    archivo = fields.Binary('Adjunto')
    ficha_id = fields.Many2one('ficha.socioeconomica')

class AyudaTerceros(models.Model):
    _name = "ayuda.tercera"
    _description = "Ayuda a Terceras Personas"

    nombre = fields.Char('Nombres Completos')
    cedula = fields.Char('Cédula')
    ingresos = fields.Float('Ingresos',digits=(4,2))
    fuente = fields.Char('Fuente')
    ficha_id = fields.Many2one('ficha.socioeconomica')

class FamiliaresIngresos(models.Model):
    _name = "familiar.ingresos"
    _description = "Familiares o personas que generan ingresos para el sustento del hogar"

    nombre = fields.Char('Nombres Completos')
    cedula = fields.Char('Cédula')
    ingresos = fields.Float('Ingresos',digits=(4,2))
    fuente = fields.Char('Fuente')
    parentezco = fields.Selection([
        ('a', 'Abuelo/a'),
        ('c', 'Conyugue'),
        ('h', 'Hermano/a'),
        ('hj', 'Hijo/a'),
        ('m', 'Madre'),
        ('p', 'Padre'),
        ('s', 'Sobrino/a'),
        ('t', 'Tio/a'),
        ('o', 'Otros'),
    ], 'Parentesco', required=True, default='o')
    ficha_id = fields.Many2one('ficha.socioeconomica')

class Vehiculos(models.Model):
    _name = "vehiculos"
    _description = "Vehículos"

    placa = fields.Char('Placa')
    modelo = fields.Char('Modelo')
    marca = fields.Char('Marca')
    tipo_vehiculo = fields.Selection([
        ('a', 'Automóvil'),
        ('c', 'Camioneta'),
        ('f', 'Furgoneta'),
        ('cg', 'Camion'),
        ('v', 'Volqueta'),
        ('o', 'Otros'),

    ], 'Tipo Vehiculo', required=True, default='a')
    valor = fields.Float('Valor', digits=(6,2))
    ficha_id = fields.Many2one('ficha.socioeconomica')

class Viviendas(models.Model):
    _name = "vivienda"
    _description = "Bienes inmuebles"

    tipo_casa = fields.Selection([
        ('l', 'Lote'),
        ('c', 'Casa'),
        ('f', 'Finca'),
        ('o', 'Otros'),

    ], 'Tipo Inmuebles', required=True, default='o')
    pais = fields.Many2one('res.country', 'Pais')
    provincia = fields.Char(string="Provincia")
    canton = fields.Char(string="Canton")
    parroquia = fields.Char(string="Parroquia")
    direccion = fields.Char("Dirección")
    anno = fields.Integer("Año de adquisición")
    valor = fields.Float('Valor', digits=(6,2))
    ficha_id = fields.Many2one('ficha.socioeconomica')


class ModeloMatIngresos(models.Model):
    _name = "mat.ingresos"
    _description = "Modelo Ingresos Totales"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Rango')
    min_value = fields.Float('Valor Minimo')
    max_value = fields.Float('Valor Maximo')
    ponderacion = fields.Integer('Ponderacion')


class ModeloMatDiscapacidad(models.Model):
    _name = "mat.discapacidad"
    _description = "Modelo Discapacidad"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Variables')
    ponderacion = fields.Integer('Ponderacion')


class ModeloMatEnfermedad(models.Model):
    _name = "mat.enfermedad"
    _description = "Modelo enfermedad"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Variables')
    ponderacion = fields.Integer('Ponderacion')


class ModeloMatFamilia(models.Model):
    _name = "mat.familia"
    _description = "Modelo familia"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Variables')
    ponderacion = fields.Integer('Ponderacion')


class ModeloMatHogar(models.Model):
    _name = "mat.hogar"
    _description = "Modelo hogar"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Variables')
    ponderacion = fields.Integer('Ponderacion')