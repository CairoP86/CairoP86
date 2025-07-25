Public Class Form1
    Private Sub btnCalcular_Click(sender As Object, e As EventArgs) Handles btnCalcular.Click
        ' Validar que los campos no estén vacíos
        If String.IsNullOrWhiteSpace(txtNombre.Text) OrElse _
           String.IsNullOrWhiteSpace(txtNota1.Text) OrElse _
           String.IsNullOrWhiteSpace(txtNota2.Text) OrElse _
           String.IsNullOrWhiteSpace(txtNota3.Text) Then
            MessageBox.Show("Todos los campos son obligatorios", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            Return
        End If

        ' Validar y convertir las notas
        Dim nota1, nota2, nota3 As Double
        If Not Double.TryParse(txtNota1.Text, nota1) OrElse nota1 < 0 OrElse nota1 > 100 Then
            MessageBox.Show("Nota 1 debe ser un número entre 0 y 100", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            txtNota1.Focus()
            Return
        End If
        If Not Double.TryParse(txtNota2.Text, nota2) OrElse nota2 < 0 OrElse nota2 > 100 Then
            MessageBox.Show("Nota 2 debe ser un número entre 0 y 100", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            txtNota2.Focus()
            Return
        End If
        If Not Double.TryParse(txtNota3.Text, nota3) OrElse nota3 < 0 OrElse nota3 > 100 Then
            MessageBox.Show("Nota 3 debe ser un número entre 0 y 100", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            txtNota3.Focus()
            Return
        End If

        ' Calcular el promedio
        Dim promedio As Double = (nota1 + nota2 + nota3) / 3
        Dim estado As String = If(promedio >= 70, "APROBADO", "REPROBADO")

        ' Mostrar el resultado
        lblResultado.Text = $"{txtNombre.Text} obtiene un promedio de {promedio:F1} y ha {estado}."
    End Sub
End Class
