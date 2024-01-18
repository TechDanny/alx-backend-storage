-- lists all the bands with Glam rock
SELECT band_name, COALESCE(split, 2020) - formed AS lifespan FROM
metal_bands WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;