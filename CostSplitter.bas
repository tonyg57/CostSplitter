'Cost splitter calculator for 2 or 3-way splits
'Derived from my MC travel Excel formulas
'V2.0 :: 27-OCT-23 :: tonyg57
'Re-organized with Select Case in Do Loop to eliminate GoTo methodology
'
_Title "2 & 3 Way Cost Splitter V2"
'--------------------------------
Do
    Color 2, 0
    Print: Print "Is this a 2-way or 3-way split (type 2 or 3, 'q' to quit): ";
    Input SplitType$

    Select Case SplitType$
        Case "2"
            GoSub TwoWaySplit
        Case "3"
            GoSub ThreeWaySplit
        Case "q", "Q"
            Color 12, 0
            Print "Exiting..."
            _Delay 1
            System
        Case Else
            Color 12, 0
            Print "Bad input: answer '2', '3', or 'q' to quit"
    End Select

Loop While SplitType$ <> "q" And SplitType$ <> "Q"
'-------------------------------------------------
TwoWaySplit:

Color 14, 0
Print: Print "2-way cost split": Print

Input "First person's name"; Person1$
If Person1$ = "" Then Person1$ = "Tony"
Print "Total amount "; Person1$; " has paid: ";
Input Person1Paid

Input "Second person's name"; Person2$
If Person2$ = "" Then Person2$ = "Partner"
Print "Total amount "; Person2$; " has paid: ";
Input Person2Paid

EvenSplit = (Person1Paid + Person2Paid) / 2

Print: Print "* Total cost is: "; Using " $###.##"; Person1Paid + Person2Paid
Print "* The even split amount is: "; Using " $###.##"; EvenSplit

If Person1Paid - EvenSplit < 0 Then
    Print "* "; Person1$; " owes "; Person2$; Using " $###.##"; Abs(EvenSplit - Person1Paid)
ElseIf Person1Paid - EvenSplit > 0 Then
    Print "* "; Person2$; " owes "; Person1$; Using " $###.##"; Abs(EvenSplit - Person1Paid)
ElseIf Person1Paid - EvenSplit = 0 Then
    Print "* This is an even split."
End If

Print 'blank line
Return
'-------------------------------------------------
ThreeWaySplit:

Color 11, 0
Print: Print "3-way cost split": Print

Input "First person's name"; Person1$
If Person1$ = "" Then Person1$ = "Tony"
Print "Total amount "; Person1$; " has paid: ";
Input Person1Paid

Input "Second person's name"; Person2$
If Person2$ = "" Then Person2$ = "Gary"
Print "Total amount "; Person2$; " has paid: ";
Input Person2Paid

Input "Third person's name"; Person3$
If Person3$ = "" Then Person3$ = "Bill"
Print "Total amount "; Person3$; " has paid: ";
Input Person3Paid

'Using 'Person#Share' to simplify 3 parameter If code below. Using negative to avoid changing all the <= & >=
EvenSplit = (Person1Paid + Person2Paid + Person3Paid) / 3
Person1Share = -1 * (EvenSplit - Person1Paid): Person2Share = -1 * (EvenSplit - Person2Paid): Person3Share = -1 * (EvenSplit - Person3Paid)

Print: Print "* Total cost is: "; Using " $###.##"; Person1Paid + Person2Paid + Person3Paid
Print "* The even split amount is: "; Using " $###.##"; EvenSplit

'One person covered all costs and then avoid running the two or more If block below since another match will occur.
If Person1Paid > 0 And Person2Paid = 0 And Person3Paid = 0 Then 'Person1 paid
    Print "* "; Person2$; " and "; Person3$; " each owe "; Person1$; Using " $###.##"; EvenSplit
    Return
ElseIf Person1Paid = 0 And Person2Paid > 0 And Person3Paid = 0 Then 'Person2 paid
    Print "* "; Person1$; " and "; Person3$; " each owe "; Person2$; Using " $###.##"; EvenSplit
    Return
ElseIf Person1Paid = 0 And Person2Paid = 0 And Person3Paid > 0 Then 'Person3 paid
    Print "* "; Person1$; " and "; Person2$; " each owe "; Person3$; Using " $###.##"; EvenSplit
    Return
End If

'Two or more persons covered costs
If Person1Share <= 0 And Person2Share >= 0 And Person3Share <= 0 Then
    Print "* "; Person1$; " owes "; Person2$; Using " $###.##"; Abs(Person1Share)
    Print "* and "; Person3$; " owes "; Person2$; Using " $###.##"; Abs(Person3Share)
ElseIf Person1Share >= 0 And Person2Share >= 0 And Person3Share <= 0 Then
    Print "* "; Person3$; " owes "; Person1$; Using " $###.##"; Abs(Person1Share)
    Print "* and owes "; Person2$; Using " $###.##"; Abs(Person2Share)
ElseIf Person1Share >= 0 And Person2Share <= 0 And Person3Share <= 0 Then
    Print "* "; Person2$; " owes "; Person1$; Using " $###.##"; Abs(Person2Share)
    Print "* and "; Person3$; " owes "; Person1$; Using " $###.##"; Abs(Person3Share)
ElseIf Person1Share <= 0 And Person2Share <= 0 And Person3Share >= 0 Then
    Print "* "; Person1$; " owes "; Person3$; Using " $###.##"; Abs(Person1Share)
    Print "* and "; Person2$; " owes "; Person3$; Using " $###.##"; Abs(Person2Share)
ElseIf Person1Share <= 0 And Person2Share >= 0 And Person3Share >= 0 Then
    Print "* "; Person1$; " owes "; Person2$; Using " $###.##"; Abs(Person2Share)
    Print "* and owes "; Person3$; Using " $###.##"; Abs(Person3Share)
ElseIf Person1Share >= 0 And Person2Share <= 0 And Person3Share >= 0 Then
    Print "* "; Person2$; " owes "; Person1$; Using " $###.##"; Abs(Person1Share)
    Print "* and owes "; Person3$; Using " $###.##"; Abs(Person3Share)
End If

Print 'blank line
Return
