import os.path
import unittest
from six import BytesIO

from qiime_default_reference import (
    get_reference_sequences, get_reference_taxonomy, get_reference_tree,
    get_template_alignment, get_template_alignment_column_mask, safe_md5,
    _get_reference_data)


class TestInit(unittest.TestCase):
    def test_get_reference_sequences(self):
        fp = get_reference_sequences()
        self.assertIn(
            os.path.join('gg_13_8_otus', 'rep_set', '97_otus.fasta'), fp)
        self.assertTrue(os.path.isfile(fp))
        self.assertTrue(os.path.isabs(fp))

        with open(fp, 'rb') as f:
            md5 = safe_md5(f).hexdigest()
        self.assertEqual(md5, '50b2269712b3738afb41892bed936c29')

    def test_get_reference_taxonomy(self):
        fp = get_reference_taxonomy()
        self.assertIn(
            os.path.join('gg_13_8_otus', 'taxonomy', '97_otu_taxonomy.txt'), fp)
        self.assertTrue(os.path.isfile(fp))
        self.assertTrue(os.path.isabs(fp))

        with open(fp, 'rb') as f:
            md5 = safe_md5(f).hexdigest()
        self.assertEqual(md5, '56ef15dccf2e931ec173f4f977ed649b')

    def test_get_reference_tree(self):
        fp = get_reference_tree()
        self.assertIn(
            os.path.join('gg_13_8_otus', 'trees', '97_otus.tree'), fp)
        self.assertTrue(os.path.isfile(fp))
        self.assertTrue(os.path.isabs(fp))

        with open(fp, 'rb') as f:
            md5 = safe_md5(f).hexdigest()
        self.assertEqual(md5, 'b7e76593bce82913af1cfb06edf15732')

    def test_get_template_alignment(self):
        fp = get_template_alignment()
        self.assertIn(
            os.path.join('gg_13_8_otus', 'rep_set_aligned', '85_otus.pynast.fasta'),
            fp)
        self.assertTrue(os.path.isfile(fp))
        self.assertTrue(os.path.isabs(fp))

        with open(fp, 'rb') as f:
            md5 = safe_md5(f).hexdigest()
        self.assertEqual(md5, '1de2e593b38041c5b3012220325b76fa')

    def test_get_template_alignment_column_mask(self):
        # make sure the literal Lane mask matches the real file's MD5 (without
        # the trailing newline)
        exp = 'e3e5f2804e29694e03a01fd9cc157a53'
        obs = safe_md5(
            BytesIO(get_template_alignment_column_mask())).hexdigest()
        self.assertEqual(obs, exp)

    # Copied and modified from
    # https://github.com/biocore/scikit-bio/blob/master/skbio/util/tests/test_misc.py
    # See licenses/scikit-bio.txt for more details.
    def test_safe_md5(self):
        exp = 'ab07acbb1e496801937adfa772424bf7'
        fd = BytesIO(b'foo bar baz')
        obs = safe_md5(fd)
        self.assertEqual(obs.hexdigest(), exp)
        fd.close()

    def test_get_reference_data(self):
        with self.assertRaises(IOError):
            _get_reference_data('this', 'file', 'hopefully', 'doesn\'t',
                                'exist')


if __name__ == '__main__':
    unittest.main()
