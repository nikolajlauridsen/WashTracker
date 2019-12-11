using System;
using System.Collections.Generic;
using System.Text;
using Microsoft.EntityFrameworkCore;

namespace WashLib.Models
{
    public class WashContext : DbContext
    {
        public WashContext() { }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            optionsBuilder.UseSqlite("Data Source=Wash.db");
        }

        public DbSet<Wash> Washes { get; set; }
        public DbSet<Receipt> Receipts { get; set; }
    }
}
