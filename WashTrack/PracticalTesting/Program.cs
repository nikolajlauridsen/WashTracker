using System;
using System.Collections.Generic;
using System.Linq;
using Microsoft.EntityFrameworkCore;
using WashLib.Models;

namespace PracticalTesting
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Washes!");
            WashContext context = new WashContext();

            List<Wash> paidWashes = context.Washes.Where(w => w.ReceiptID != null).ToList();
            List<Wash> unpaidWashes = context.Washes.Where(w => w.ReceiptID == null).ToList();


            Console.WriteLine($"Paid washes, Amount: {paidWashes.Count}");
            foreach (Wash wash in paidWashes)
            {
                Console.WriteLine($"Date: {wash.Date.ToString()}\tPrice: {wash.Price}");
            }

            Console.WriteLine($"\n\nUnpaid washes, Amount: {unpaidWashes.Count}");
            foreach (Wash wash in unpaidWashes)
            {
                Console.WriteLine($"Date: {wash.Date.ToString()}\tPrice: {wash.Price}");
            }

            Console.WriteLine("\n\nReceipts: ");
            List<Receipt> receipts = context.Receipts.Include(r => r.Washes).ToList();
            foreach (Receipt receipt in receipts)
            {
                Console.WriteLine($"Receipt paid {receipt.Date}\nContains washes:");
                foreach (Wash wash in receipt.Washes)
                {
                    Console.WriteLine($"Date: {wash.Date.ToString()}\tPrice: {wash.Price}");
                }

                Console.WriteLine($"Total: {receipt.Total}");
            }
        }
    }
}
