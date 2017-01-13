
BULK INSERT Committees
    FROM '../../jam4changedata/committees.csv'
    WITH
    (
    FIRSTROW = 2,
    FIELDTERMINATOR = '|',  --CSV field delimiter
    ROWTERMINATOR = '\r\n',   --Use to shift the control to next row
    ERRORFILE = 'committees.sql.err.csv',
    TABLOCK
    )

--http://stackoverflow.com/questions/15242757/import-csv-file-into-sql-server