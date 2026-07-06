# Relational Schema & Lineage Mapping

Defines relational entities, source grains, key relationships, and source of truth policies for database integration.

| Path | Title | Type | Description |
|------|-------|------|-------------|
| catalog/relational-schema-and-lineage/denormalization-and-source-of-truth-policy | Denormalization & Source of Truth Policy | file | Establishes that the canonical products catalog table is the authoritative source when attributes conflict with denormalized product columns in inventory items. |
| catalog/relational-schema-and-lineage/table-grains-and-keys | Table Grains and Keys | file | Maps keys and defines rows for core physical tables including users, orders, order items, products, inventory items, and distribution centers. |
