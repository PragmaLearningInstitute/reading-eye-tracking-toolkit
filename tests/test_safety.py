import csv, io, sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from safety import safe_identifier, safe_csv_writer, spreadsheet_safe

class ExportSafety(unittest.TestCase):
    def test_formula_cells_remain_text(self):
        values = ['=1+1', '+SUM(A1:A2)', '-SUM(A1:A2)', '@SUM(A1)', '  =1', '\t=1']
        stream = io.StringIO(); safe_csv_writer(stream).writerow(values)
        self.assertTrue(all(x.startswith("'") for x in next(csv.reader(io.StringIO(stream.getvalue())))))
    def test_numeric_measurements_survive(self):
        for value in ['-0.052', '+1.0', '1e-3', 1.5, '', 'Bonjour']:
            self.assertEqual(spreadsheet_safe(value), value)
    def test_identifiers_cannot_be_paths(self):
        self.assertEqual(safe_identifier('DEMO_001-A'), 'DEMO_001-A')
        for value in ['../person', '/tmp/a', 'a/b', 'a\\b', '', '=A1', 'a'*65]:
            with self.assertRaises(ValueError): safe_identifier(value)

if __name__ == '__main__': unittest.main()
