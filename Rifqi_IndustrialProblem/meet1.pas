program belajar_pascal;

type
        IntegerArray = Array of Integer;
        IntegerDoubleArray = Array of Array of Integer;

function power_int(num1, num2: Integer): Integer;
        var
                i, Result:Integer;
        begin
                Result := 1;
                for i:=1 to num2 do
                        Result:=Result*num1;
                power_int:=Result
        end;

(*function that return all combinations and summed up*)
function combination_util(feeder_array: array of integer): IntegerArray;
        var
                i,j, B, C, count, reset_index: Integer;
                temp_poin: Integer;
                Result: Array of Integer;
        begin
                count := power_int(2,Length(feeder_array));

                SetLength(Result, count);

                for i:= 0 to count-1 do
                begin
                        temp_poin:=0;
                        for j:= 0 to Length(feeder_array)-1 do
                        begin
                                B:=1<<j;
                                C:=(i and B);
                                //writeln(C<>0);
                                if (C <> 0) then
                                begin
                                        temp_poin:=temp_poin+feeder_array[j];
                                end;
                        end;
                        Result[i]:=temp_poin;
                end;
                combination_util:=Result;
        end;

(*function that return the index*)
function finding_index(feeder_combination:Array of Integer; source_loss:Integer): Integer;
        var i, Result:Integer;
        begin
                for i:=0 to Length(feeder_combination) do
                        begin
                                if (feeder_combination[i]=source_loss) then
                                        begin
                                                Result:=i;
                                                Break;
                                        end;
                        end;
                finding_index:=Result;
        end;

(*function that return all combinations index*)
function combination_index(feeder_array: array of integer): IntegerDoubleArray;
        var
                i,j, B, C, count, reset_index: Integer;
                Result: Array of Array of Integer;
        begin
                count := power_int(2,Length(feeder_array));

                SetLength(Result, count, Length(feeder_array));

                for i:= 0 to count-1 do
                begin
                        for j:= 0 to Length(feeder_array)-1 do
                        begin
                                B:=1<<j;
                                C:=(i and B);
                                if (C <> 0) then
                                begin
                                        Result[i][j]:=feeder_array[j];
                                end;
                        end;
                end;
                combination_index:=Result;
        end;

const
        //power_source = 50;
        power_loss = 50;
var
        i, count, index_opt : Integer;
        feeder: array [0..6] of integer;
        feeder_combination: Array of Integer;
        array_index_combination: Array of Array of Integer;
begin
        feeder[0]:=11;
        feeder[1]:=7;
        feeder[2]:=25;
        feeder[3]:=5;
        feeder[4]:=33;
        feeder[5]:=14;
        feeder[6]:=9;
        count:= power_int(2,Length(feeder));
        //writeln(count);

        setLength(feeder_combination, count);
        feeder_combination:=combination_util(feeder);
        //for i:= 0 to count do
        //begin
        //        writeln(feeder_combination[i]);
        //end;

        array_index_combination:=combination_index(feeder);
        index_opt:=finding_index(feeder_combination, power_loss);
        //writeln(index_opt);

        for i:=0 to Length(feeder) do
        begin
                writeln(array_index_combination[index_opt][i])
        end;
end.