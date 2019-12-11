using System;
using System.Collections.Generic;
using System.Text;

namespace WashLib.Models
{
    public class Wash
    {
        public int ID { get; set; }

        public int? ReceiptID { get; set; }

        public DateTime Date { get; set; }

        public double Price { get; set; }
    }
}
