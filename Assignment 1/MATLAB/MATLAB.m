files = dir('../matrici/*.mat');
csv = ["Nome", "Dimensione", "Tempo (s)", "Errore relativo"];

for i=1:length(files)
  time = "Errore"; error = "Errore"; sizeMat = 0;
  try
    file = char(['../matrici/',files(i).name]);
    
    disp(['File ', file])
    disp('| Preparazione variabili')
    tic();
    load(file);
    
    A = Problem.A;
    sizeMat = size(A,1);
    xe = ones(1,sizeMat)';

    b = A*xe;
    time = toc;
    disp(['| Tempo per preparare le variabili ', num2str(time)])
    
    disp('| Calcolo soluzione')
    tic
    x = A\b;
    time = toc;
    disp(['| Tempo per calcolare la soluzione ', num2str(time)]) 
    
    error = norm(x-xe) / norm(xe);   
    disp(['| Errore relativo: ', num2str(error)])
  catch exception
    disp(['| Eccezione: ', exception.message]);
  end
  runInfo = {files(i).name, sizeMat, time, error};
  csv = [csv; runInfo];
end
writematrix(csv, "reportMatlab.csv");
disp("Fine");