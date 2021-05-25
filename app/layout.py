import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt
from app import app
from app.models import Utilization


app.layout = html.Div(id='app_container', style={'minHeight':'100%', 'maxHeight':'100%', 'minWidth':'25%', 'maxWidth':'100%', 'display':'flex', 'flexDirection':'row', 'alignItems':'flex-start', 'padding':'0 1rem'},
                      children=[
                          html.Div(id='menu_section', style={'minHeight':'100%', 'maxHeight':'100%', 'minWidth':'25%', 'maxWidth':'25%', 'display':'flex', 'flexDirection':'column', 'alignItems':'flex-start', 'padding':'1.25rem 1rem'},
                                   children=[
                                       html.Div(id='selection_section', style={'minWidth':'100%', 'maxWidth':'100%', 'display':'flex', 'flexDirection':'column', 'alignItems':'flex-start', 'padding':'0 1rem'},
                                                children=[
                                                    html.Div(id='rank_position_section', style={'minWidth':'100%', 'maxWidth':'100%', 'display':'flex', 'flexDirection':'row', 'alignItems':'flex-start', 'padding':'0 1rem'},
                                                             children=[
                                                                 html.P(id='rank_position_label', style={'width':'12.5rem'}, children=['Rank Position']),
                                                                 dcc.Dropdown(id='rank_position_dropdown', options=[{'label': result, 'value': result} for result in ('Top', 'Bottom')], value='Top', style={'minWidth':'12.5rem'}, clearable=False)
                                                             ]
                                                             ),
                                                    html.Div(id='rank_by_section', style={'minWidth':'100%', 'maxWidth':'100%', 'display': 'flex', 'flexDirection': 'row', 'alignItems': 'flex-start', 'padding': '0 1rem'},
                                                             children=[
                                                                 html.P(id='rank_by_label', style={'width':'12.5rem'}, children=['Rank By']),
                                                                 dcc.Dropdown(id='rank_by_dropdown', options=[{'label':result, 'value':result} for result in ('Avg Charged', 'Patients')], value='Avg Charged', style={'minWidth':'12.5rem'}, clearable=False)
                                                             ]
                                                             ),
                                                    html.Div(id='state_section', style={'minWidth':'100%', 'maxWidth':'100%', 'display': 'flex', 'flexDirection': 'row', 'alignItems': 'flex-start', 'padding': '0 1rem'},
                                                             children=[
                                                                 html.P(id='state_label', style={'width':'12.5rem'}, children=['State']),
                                                                 dcc.Dropdown(id='state_dropdown', options=[{'label':result[0], 'value':result[0]} for result in Utilization.query.with_entities(Utilization.state).group_by(Utilization.state).order_by(Utilization.state)], value='TN', placeholder='(all)', style={'minWidth':'12.5rem'}, multi=True)
                                                             ]
                                                             ),
                                                    html.Div(id='city_section', style={'minWidth':'100%', 'maxWidth':'100%', 'display': 'flex', 'flexDirection': 'row', 'alignItems': 'flex-start', 'padding': '0 1rem'},
                                                             children=[
                                                                 html.P(id='city_label', style={'width':'12.5rem'}, children=['City']),
                                                                 dcc.Dropdown(id='city_dropdown', placeholder='(all)', style={'minWidth':'12.5rem'}, multi=True)
                                                             ]
                                                             ),
                                                    html.Div(id='zip_code_section', style={'minWidth':'100%', 'maxWidth':'100%', 'display': 'flex', 'flexDirection': 'row', 'alignItems': 'flex-start', 'padding': '0 1rem'},
                                                             children=[
                                                                 html.P(id='zip_code_label', style={'width':'12.5rem'}, children=['Zip Code']),
                                                                 dcc.Dropdown(id='zip_code_dropdown', placeholder='(all)', style={'minWidth':'12.5rem'}, multi=True)
                                                             ]
                                                             ),
                                                    html.Div(id='place_of_service_section', style={'minWidth':'100%', 'maxWidth':'100%', 'display': 'flex', 'flexDirection': 'row', 'alignItems': 'flex-start', 'padding': '0 1rem'},
                                                             children=[
                                                                 html.P(id='place_of_service_label', style={'width':'12.5rem'}, children=['Place of Service']),
                                                                 dcc.Dropdown(id='place_of_service_dropdown', placeholder='(all)', style={'minWidth':'12.5rem'}, multi=True)
                                                             ]
                                                             ),
                                                    html.Div(id='provider_type_section', style={'minWidth':'100%', 'maxWidth':'100%', 'display': 'flex', 'flexDirection': 'row', 'alignItems': 'flex-start', 'padding': '0 1rem'},
                                                             children=[
                                                                 html.P(id='provider_type_label', style={'width':'12.5rem'}, children=['Provider Type']),
                                                                 dcc.Dropdown(id='provider_type_dropdown', placeholder='(all)', style={'minWidth':'12.5rem'}, multi=True)
                                                             ]
                                                             ),
                                                    html.Div(id='credential_section', style={'minWidth':'100%', 'maxWidth':'100%', 'display': 'flex', 'flexDirection': 'row', 'alignItems': 'flex-start', 'padding': '0 1rem'},
                                                             children=[
                                                                 html.P(id='credential_label', style={'width':'12.5rem'}, children=['Credential']),
                                                                 dcc.Dropdown(id='credential_dropdown', placeholder='(all)', style={'minWidth':'12.5rem'}, multi=True)
                                                             ]
                                                             ),
                                                    html.Div(id='hcpcs_code_section', style={'minWidth':'100%', 'maxWidth':'100%', 'display': 'flex', 'flexDirection': 'row', 'alignItems': 'flex-start', 'padding': '0 1rem'},
                                                             children=[
                                                                 html.P(id='hcpcs_code_label', style={'width':'12.5rem'}, children=['HCPCS Code']),
                                                                 dcc.Dropdown(id='hcpcs_code_dropdown', placeholder='(all)', style={'minWidth':'12.5rem'}, multi=True)
                                                             ]
                                                             ),
                                                    html.Div(id='hcpcs_description_checkbox_section', style={'minWidth': '100%', 'maxWidth': '100%', 'display': 'flex', 'flexDirection': 'row', 'alignItems': 'flex-start', 'padding': '0 1rem'},
                                                             children=[
                                                                 html.P(id='hcpcs_description_checkbox_label', style={'width': '16rem', 'font-style':'italic', 'font-size':'12px', 'font-weight':400, 'font-family':['Open Sans', 'HelveticaNeue', 'Helvetica Neue', 'Helvetica', 'Arial', 'sans-serif'], 'padding':'.5rem 0 0 1.2rem'}, children=['Display HCPCS Descriptions']),
                                                                 dcc.Checklist(id='hcpcs_description_checkbox', options=[{'label': '', 'value': 'yes'}], style={'padding':'.3rem 0 0 0'})
                                                             ]
                                                             ),
                                                    dcc.Textarea(id='hcpcs_description_textbox', hidden=True, readOnly=True, style={'minHeight':'30rem', 'maxHeight':'30rem', 'minWidth':'100%', 'maxWidth':'100%', 'font-size':'14.5px', 'line-height':'1.6', 'font-weight':400, 'font-family':['Open Sans', 'HelveticaNeue', 'Helvetica Neue', 'Helvetica', 'Arial', 'sans-serif'], 'padding': '0 1.2rem'}),
                                                ]
                                                ),
                                       html.Div(id='button_section', style={'minWidth':'100%', 'maxWidth':'100%', 'display':'flex', 'flexDirection':'row', 'alignItems':'flex-start', 'padding':'3rem 1rem'},
                                                children=[
                                                    html.Button(id='submit_button', type='button', children=['Submit']),
                                                    html.A(id='export_link', href='', style={'display':'none'}, children=[html.Button(id='export_button', type='button', children=['Export'])])
                                                ]
                                                ),
                                        html.Div(id='about_section', style={'minWidth':'100%', 'maxWidth':'100%', 'display':'flex', 'flexDirection':'row', 'alignItems':'flex-start', 'padding':'0rem 1rem'},
                                                 children=[
                                                    html.A(id='about_link', href='https://github.com/d-s-1/providers_dashboard#readme', target="_blank", children='About this app', style={'font-size':'13px', 'font-weight':400, 'font-family':['Open Sans', 'HelveticaNeue', 'Helvetica Neue', 'Helvetica', 'Arial', 'sans-serif']})
                                                 ]
                                                 )
                                   ]
                                   ),
                          html.Div(id='result_section', style={'minHeight':'100%', 'maxHeight':'100%', 'minWidth':'75%', 'maxWidth':'75%', 'display':'flex', 'flexDirection':'column', 'alignItems':'flex-start', 'padding':'0 1rem'},
                                   children=[
                                       dcc.ConfirmDialog(id='required_inputs_message'),
                                       html.Div(id='results_container', style={'minHeight':'100%', 'maxHeight':'100%', 'minWidth':'100%', 'maxWidth':'100%'},
                                                children=[
                                                    html.Div(id='ten_table_section',
                                                             style={'minWidth': '65%', 'maxWidth': '65%'},
                                                             children=[
                                                                 html.Label(id='ten_table_title', children='', style={'font-size':'17px', 'line-height':'1.6', 'font-weight':400, 'font-family':['Open Sans','verdana','arial','sans-serif'], 'text-align':'center'}),
                                                                 dt.DataTable(id='ten_table', columns=[{'id': x, 'name': y} for x, y in (('provider_id', 'Provider ID'),('patients', 'Patients'),('avg_charged', 'Avg Charged'),('avg_allowed', 'Avg Allowed'),('avg_paid', 'Avg Paid'))],
                                                                              style_cell={'textAlign': 'left'}, style_cell_conditional=[{'if': {'column_id': 'provider_id'},'width': '16.6%'},{'if': {'column_id': 'patients'},'width': '16.6%'},{'if': {'column_id': 'avg_charged'},'width': '16.6%'},{'if': {'column_id': 'avg_allowed'},'width': '16.6%'},{'if': {'column_id': 'avg_paid'},'width': '16.6%'}],
                                                                              style_as_list_view=True, style_data_conditional=[{'if': {'row_index': 'odd'},'backgroundColor': 'rgb(248, 248, 248)'}], style_header={'fontWeight': 'bold'}, style_table={'padding': '.5rem 0 0 0'})
                                                             ]
                                                             ),
                                                    html.Div(id='bar_chart_section', style={'minWidth': '50%', 'maxWidth': '50%', 'padding': '4rem 0 0 0'},
                                                             children=[
                                                                 dcc.Graph(id='bar_chart', config={'displayModeBar': False})
                                                             ]
                                                             )
                                                ]),
                                       html.Div(id='spinner_container', style={'display':'none'},
                                                children=[
                                                   html.Div(id='spinner', className='spinner', style={'minHeight':'50%', 'maxHeight':'50%', 'minWidth':'50%', 'maxWidth':'50%', 'display':'flex', 'flexDirection':'row-reverse', 'justify-content':'center', 'align-items':'flex-end'},
                                                            children=[
                                                                html.Div(id='spin1'),
                                                                html.Div(id='spin2'),
                                                                html.Div(id='spin3'),
                                                                html.Div(id='spin4'),
                                                                html.Div(id='spin5'),
                                                                html.Div(id='spin6'),
                                                                html.Div(id='spin7'),
                                                                html.Div(id='spin8'),
                                                                html.Div(id='spin9'),
                                                                html.Div(id='spin10'),
                                                                html.Div(id='spin11'),
                                                                html.Div(id='spin12')
                                                    ]
                                                    )
                                                ]),
                                       dcc.Store(id='memory_store', data={'loaded': 0})
                                   ]
                                   )
                          ]
                      )