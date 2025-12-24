import dagster as dg


@dg.asset
def rawg(context: dg.AssetExecutionContext) -> dg.MaterializeResult: ...
