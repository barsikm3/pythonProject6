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

Sub InsertDataIntoFilteredRows()

Dim ws As Worksheet
Set ws = ActiveSheet

With ws
    Dim visibleRange As Range
    Set visibleRange = .Range("A1", .Cells(.Rows.Count, 1).End(xlUp)).SpecialCells(xlCellTypeVisible)
    
    Dim cell As Range
    For Each cell In visibleRange
        cell.Value = "Inserted Data"
    Next cell
End With

End SubSub InsertDataIntoFilteredRows()

Dim ws As Worksheet
Set ws = ActiveSheet

With ws
    Dim lastRow As Long
    lastRow = .Cells(.Rows.Count, 1).End(xlUp).Row
    
    Dim i As Long
    For i = 1 To lastRow
        If Not .Rows(i).Hidden Then
            .Cells(i, 1).Value = "Inserted Data"
        End If
    Next i
End With

End Sub


