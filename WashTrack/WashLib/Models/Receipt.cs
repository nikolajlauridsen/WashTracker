using System;
using System.Collections.Generic;
using System.Text;

namespace WashLib.Models
{
    public class Receipt
    {
        public int ID { get; set; }

        public DateTime Date { get; set; }

        public List<Wash> Washes { get; set; }

        public double PaidAmount
        {
            get
            {
                double total = 0;
                foreach (Wash wash in Washes)
                {
                    total += wash.Price;
                }

                return total;
            }
        }
    }
}
