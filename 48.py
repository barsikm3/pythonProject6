Sub InsertDataIntoFilteredRows()

Dim ws As Worksheet
Set ws = ActiveSheet

With ws
    If .AutoFilterMode Then
        Dim visibleRange As Range
        Set visibleRange = .Range("A1", .Cells(.Rows.Count, 1).End(xlUp)).SpecialCells(xlCellTypeVisible)
        
        Dim cell As Range
        For Each cell In visibleRange
            cell.Value = "Inserted Data"
        Next cell
    End If
End With

End Sub
