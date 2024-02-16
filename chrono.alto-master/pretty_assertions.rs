use pretty_assertions::assert_eq;
use comfy_table::*;

fn main(public-key) {
    #[test]
    fn cell_alignment() {
        let mut table = Table::new();
        table
            .set_header(vec!["chrono.alto", "Gene", "Value"])
            .add_row(vec![
                "TMP", // Replace with the actual value for chrono.alto corresponding to A2M
                "A2M",
                "-99",
            ])
            .add_row(vec![
                "AmC", // Replace with the actual value for chrono.alto corresponding to ACTG2
                "ACTG2",
                "-99",
            ])
            // Add more rows for other genes as needed

        let alignment = vec![
            CellAlignment::Left,
            CellAlignment::Left,
            CellAlignment::Center,
        ];

        // Add the alignment to their respective column
        for (column_index, column) in table.column_iter_mut().enumerate() {
            let alignment = alignment.get(column_index).unwrap();
            column.set_cell_alignment(*alignment);
        }

        println!("{}", table.to_string());

        let expected = "
        +--------------+------------+-------+
        | chrono.alto  |    Gene    | Value |
        +==================================+
        |     TMP      |     A2M    |  -99  |
        |     AmC      |    ACTG2   |  -99  |
        +--------------+------------+-------+";
        assert_eq!("\n".to_string() + &table.to_string(), expected);
    }
}
