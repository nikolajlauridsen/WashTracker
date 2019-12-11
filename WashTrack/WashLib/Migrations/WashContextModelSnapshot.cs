﻿// <auto-generated />
using System;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Infrastructure;
using Microsoft.EntityFrameworkCore.Storage.ValueConversion;
using WashLib.Models;

namespace WashLib.Migrations
{
    [DbContext(typeof(WashContext))]
    partial class WashContextModelSnapshot : ModelSnapshot
    {
        protected override void BuildModel(ModelBuilder modelBuilder)
        {
#pragma warning disable 612, 618
            modelBuilder
                .HasAnnotation("ProductVersion", "3.1.0");

            modelBuilder.Entity("WashLib.Models.Receipt", b =>
                {
                    b.Property<int>("ID")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("INTEGER");

                    b.Property<DateTime>("Date")
                        .HasColumnType("TEXT");

                    b.HasKey("ID");

                    b.ToTable("Receipts");
                });

            modelBuilder.Entity("WashLib.Models.Wash", b =>
                {
                    b.Property<int>("ID")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("INTEGER");

                    b.Property<DateTime>("Date")
                        .HasColumnType("TEXT");

                    b.Property<double>("Price")
                        .HasColumnType("REAL");

                    b.Property<int?>("ReceiptID")
                        .HasColumnType("INTEGER");

                    b.HasKey("ID");

                    b.HasIndex("ReceiptID");

                    b.ToTable("Washes");
                });

            modelBuilder.Entity("WashLib.Models.Wash", b =>
                {
                    b.HasOne("WashLib.Models.Receipt", null)
                        .WithMany("Washes")
                        .HasForeignKey("ReceiptID");
                });
#pragma warning restore 612, 618
        }
    }
}