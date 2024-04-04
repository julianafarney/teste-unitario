import unittest
import coverage
import webbrowser
import os
import calculadora

class calculador(unittest.TestCase):

  def calculadora (self):
        resultado = calculadora.subtracao(7,4)
        self.assertEqual(resultado, 3.0)
  
if __name__ == '__main__':
    # Criar uma instância do Coverage com o arquivo .coveragerc
    cov = coverage.Coverage(config_file='.coveragerc.txt')

    # Iniciar a medição da cobertura
    cov.start()

    # Executar os testes
    suite = unittest.TestLoader().loadTestsFromTestCase(calculador)
    unittest.TextTestRunner(verbosity=2).run(suite)

    # Encerrar a medição da cobertura após os testes
    cov.stop()

    # Salvar os dados de cobertura em um arquivo
    cov.save()
    cov.html_report(directory='htmlcov')

    # Abra o relatório no navegador
    index_file = os.path.join('htmlcov', 'index.html')
    webbrowser.open('file://' + os.path.abspath(index_file))