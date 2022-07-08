class DrugAnalyzer:
    # TODO: Part 1 - Add method(s) necessary to fulfill the requirements.
    def __init__(self, data):
        self.data = data

    def __add__(self, data):
        if len(data) != 4:
            raise ValueError('improper length on list added')
        if not all(isinstance(i, float) for i in data[1:]) or not isinstance(data[0], str):
            raise ValueError('Improper type on list added')
        self.data = self.data + [data]
        return self
    def verify_series(
        self,
        series_id: str,
        act_subst_wgt: float,
        act_subst_rate: float,
        allowed_imp: float,
    ) -> bool:
        # TODO: Part 2 - Implement this method.
        pills = [pill for pill in self.data if series_id in pill[0]]
        if pills:
            return act_subst_wgt * len(pills) - (act_subst_wgt * len(pills) * act_subst_rate) < sum(
                [i[2] for i in pills]) < act_subst_wgt * len(pills) + (
                               act_subst_wgt * len(pills) * act_subst_rate) and sum(
                [i[3] for i in pills]) < allowed_imp * sum([i[1] for i in pills])
        else:
            raise ValueError(f'There is no {series_id} series in database')
