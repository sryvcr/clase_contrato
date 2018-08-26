
import csv


class Contrato:
    '''Define objetos Contrato muy sencillos'''
    cantidadContratos = 0 #atributo estático
    def __init__(self, nombreContratista, estado="Por definir", fechaInicio="Por Definir",
                 fechaFin="Por Definir", firma="Por definir", formaPago="Por definir",
                 lugar="Por definir", dependenciaSolicitante="Por Definir", numeroAnexos=int("0"),
                 numeroClausulas=int("0"), numeroContrato=int("0"), numeroPaginas=int(0), 
                 objetivoContrato="Por definir", supervisor="Por definir", valorContrato=int("0")):
        """ Constructor de objetos contrato
            Si no se le pasan parametros contruye un contrato
            - estado, fechas, firma, forma de pago, lugar, objetivo y 
               supervisor por definir
            - numeroAnexos = 0
            - numeroClasusulas = 0
            - numeroContrato = 0
            - numeroPaginas= 0
            - valorContrato = 0.0
            Permite crear objetos contrato especificando:
            estado, fecha de inicio, fecha de finalizacion, firma, forma de pago, lugar de
            ejecucion, numero de anexos, numero de clausulas, numero del contrato, numero 
            de paginas, objetivo del contrato, supervisor y valor del contrato """
        Contrato.cantidadContratos = Contrato.cantidadContratos + 1
        self.nombreContratista = nombreContratista
        self.estado = estado
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.firma = firma
        self.formaPago = formaPago
        self.lugarEjecucion = lugar
        self.dependenciaSolicitante = dependenciaSolicitante
        self.numeroAnexos = numeroAnexos
        self.numeroClausulas = numeroClausulas
        self.numeroContrato = numeroContrato
        self.numeroPaginas = numeroPaginas
        self.objetivoContrato = objetivoContrato
        self.supervisor = supervisor
        self.valorContrato = valorContrato
        
        print("Se ha creado: ")
        print(self)
        print('\n')
    
    def verNombreContratista(self):
        """Devuelve el estado actual del contrato"""
        return (self.nombreContratista)
        
    def verEstado(self):
        """Devuelve el estado actual del contrato"""
        return (self.estado)
        
    def verFechaInicio(self):
        """Devuelve la fecha de inicio del contrato"""
        return (self.fechaInicio)
    
    def verFechaFin(self):
        """Devuelve la fecha de finalizacion del contrato"""
        return (self.fechaFin)
    
    def verFirma(self):
        """Devuelve la firma del contrato"""
        return (self.firma)
    
    def verFormaPago(self):
        """Devuelve la forma de pago del contrato"""
        return (self.formaPago)
        
    def verLugarEjecucion(self):
        """Devuelve el lugar de ejecucion del contrato"""
        return (self.lugarEjecucion)

    def verDependenciaSolicitante(self):
        """Devuelve el lugar de ejecucion del contrato"""
        return (self.dependenciaSolicitante)
        
    def verNumeroAnexos(self):
        """Devuelve el numero de anexos del contrato"""
        return (self.numeroAnexos)
        
    def verNumeroClausulas(self):
        """Devuelve el numero de clausulas del contrato"""
        return (self.numeroClausulas)
        
    def verNumeroContrato(self):
        """Devuelve el numero del contrato"""
        return (self.numeroContrato)
    
    def verNumeroPaginas(self):
        """Devuelve el numero de paginas del contrato"""
        return (self.numeroPaginas)
    
    def verObjetivoContrato(self):
        """Devuelve el objetivo del contrato"""
        return (self.objetivoContrato)
    
    def verSupervisor(self):
        """Devuelve el encargado de supervisar el contrato"""
        return (self.supervisor)
    
    def verValorContrato(self):
        """Devuelve el valor del contrato"""
        return (self.valorContrato)
    
    def __str__(self):
        """Visualiza el objeto Contrato con estado, fecha de inicio, fecha de
        finalizacion, firma, forma de pago, lugar de ejecucion, numero de anexos,
        numero de clausulas, numero de contrato, numero de paginas, objetivo del
        contrato, supervisor y valor del contrato"""
        return ("Objeto Contrato = " + '\n' 
                + " - Número de contrato: " + str(self.numeroContrato) + '\n'
                + " - Nombre del contratista: " + str(self.nombreContratista) + '\n'
                + " - Fecha de inicio: " + str(self.fechaInicio) + '\n'
                + " - Fecha de finalización: " + str(self.fechaFin) + '\n'
                + " - Estado: " + self.estado + '\n'
                + " - Firma: " + self.firma + '\n'
                + " - Forma de pago: " + self.formaPago + '\n'
                + " - Lugar de ejecución: " + self.lugarEjecucion + '\n'
                + " - Dependencia Solicitante: " + self.dependenciaSolicitante + '\n'
                + " - Número de anexos: " + str(self.numeroAnexos) + '\n'
                + " - Número de clausulas: " + str(self.numeroClausulas) + '\n'
                + " - Número de páginas: " + str(self.numeroPaginas) + '\n'
                + " - Objetivo del contrato: " + self.objetivoContrato + '\n'
                + " - Supervisor: " + self.supervisor + '\n'
                + " - Valor del contrato: $ " + str(self.valorContrato) + " COP" +''
                )
        
    @staticmethod
    def verCantidadContratos():
        return (Contrato.cantidadContratos)

def main():
    """Prueba de la clase Contrato"""
    
    nombreArchivo = "datos_simulacion.csv"
    nLinea=0

    try:
        archivoCSV = open(nombreArchivo, 'r')
        lineas = csv.reader(archivoCSV)
        for fila in lineas:
            nLinea=nLinea+1
            filaNueva = tuple(fila)
            #print("Contrato "+ str(nLinea) +" =", filaNueva)
            #Contrato(tuple(fila))
            if nLinea > 1:
                contrato1 = Contrato(filaNueva[0], filaNueva[1], filaNueva[2], filaNueva[3], filaNueva[4], 
                    filaNueva[5], filaNueva[6], filaNueva[7], filaNueva[8], filaNueva[9], filaNueva[10], 
                    filaNueva[11], filaNueva[12], filaNueva[13], filaNueva[14])
    except IOError:
        print('Error procesando el archivo ', nombreArchivo)
        exit()
    finally:
        archivoCSV.close()

    print("Numero de contratos creados (clase) = " + str(Contrato.verCantidadContratos()))
    print("Numero de contratos creados (objetos) = " + str(contrato1.verCantidadContratos()))
    print('')
    
if __name__ == "__main__":
    main()